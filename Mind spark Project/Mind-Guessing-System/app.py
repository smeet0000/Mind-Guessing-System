
from flask import Flask, render_template, request, redirect, url_for, session
import random
from config import SECRET_KEY
from utils.data_utils import load_data, filter_candidates
from utils.save_utils import save_new_entry
from utils.google_api import fetch_google_image
from utils.game_logic import make_question, pick_next_attribute, get_priority_list

app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.route("/")
def index():
    # Homepage
    return render_template("index.html")


@app.route("/select")
def select_category():
    # Category selection page
    return render_template("select.html")


@app.route("/start", methods=["POST"])
def start():
    # Start the guessing game
    category = request.form.get("category")
    if not category:
        return redirect(url_for("select_category"))

    # Initialize session data
    session.clear()
    session.update({
        "category": category,
        "asked": [],         
        "answers": {},        
        "questions_asked": 0,
        "min_q": 15         
    })
    return redirect(url_for("question"))


@app.route("/question")
def question():
    # Ask the next question
    category = session.get("category")
    if not category:
        return redirect(url_for("index"))

    data = load_data(category)
    answers = session.get("answers", {})
    asked = session.get("asked", [])
    candidates = data

    # Filter candidates based on previous answers
    for attr, ans in answers.items():
        candidates = filter_candidates(candidates, attr, ans)

    q_count = session.get("questions_asked", 0)

    #  No candidates left 
    if not candidates:
        return redirect(url_for("guess"))

    #  If exactly ONE candidate left:

    if len(candidates) == 1:
        final_item = candidates[0]             
        item_attrs = final_item.get("attrs", [])

        # Remaining attributes which are not asked
        remaining_attrs = [a for a in item_attrs if a not in asked]

        if remaining_attrs:
            attr = remaining_attrs[0]
        else:
            return redirect(url_for("guess"))

    else:
        # Use normal attribute-picking logic

        priority_list = get_priority_list(category)
        attr = pick_next_attribute(candidates, asked, category, priority_list)

        # If no more good attribute to ask 
        if not attr:
            return redirect(url_for("guess"))

    # Store question info in session
    session["current_attr"] = attr
    question_text = make_question(attr, category)

    return render_template(
        "question.html",
        question=question_text,
        attr=attr,
        num=q_count + 1
    )


@app.route("/answer", methods=["POST"])
def answer():
    # Record the user's answer and move to next question
    attr = session.get("current_attr")
    ans = request.form.get("answer")

    if not attr or not ans:
        return redirect(url_for("question"))

    # Save answer
    answers = session.get("answers", {})
    asked = session.get("asked", [])

    answers[attr] = ans
    asked.append(attr)

    session["answers"] = answers
    session["asked"] = asked
    session["questions_asked"] = session.get("questions_asked", 0) + 1

    return redirect(url_for("question"))


@app.route("/guess", methods=["GET", "POST"])
def guess():
    # Make a guess based on filtered candidates
    category = session.get("category")
    if not category:
        return redirect(url_for("index"))

    data = load_data(category)
    answers = session.get("answers", {})
    candidates = data

    # Filter candidates again before guessing
    for attr, ans in answers.items():
        candidates = filter_candidates(candidates, attr, ans)

    # If no candidates match
    if not candidates:
        return render_template("result.html", guess=None, img=None)

    # Pick random candidate from remaining
    guess_item = random.choice(candidates)
    name = guess_item["name"]

    img = fetch_google_image(name)

    # Handle user confirmation
    if request.method == "POST":
        correct = request.form.get("correct")
        if correct == "yes":
            return render_template("result.html", guess=name, correct=True, img=img)
        else:
            real_name = request.form.get("real_name")
            special_feature = request.form.get("special_feature")
            if real_name:
                save_new_entry(category, real_name, answers, special_feature)
            return render_template("result.html", guess=name, correct=False, img=img)

    return render_template("guess.html", guess=name, img=img)


if __name__ == "__main__":
    app.run(debug=True)
