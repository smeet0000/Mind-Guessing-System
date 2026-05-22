# character_que.py

def get_questions():
    """
    Returns a dictionary mapping each attribute to a natural language question.
    Covers entertainment, social media, sports, history, mythology, politics, and tech.
    Automatically supports gender-based phrasing and mythological logic.
    """
    return {
        # Base identity
        "real": "Is this a real person?",
        "animated": "Is this an animated character?",
        "male": "Is this person male?",
        "female": "Is this person female?",

        # Entertainment & Cinema
        "bollywood": "Is this person associated with Bollywood?",
        "hollywood": "Is this person associated with Hollywood?",
        "tollywood": "Is this person part of the South Indian film industry?",
        "tv_actor": "Is this person famous for Indian TV shows?",
        "ott_star": "Is this person popular on OTT platforms like Netflix or Prime Video?",
        "cartoon": "Is this person a cartoon character?",

        # Professions & Roles
        "actor": "Is this person an actor?",
        "director": "Is this person a director?",
        "producer": "Is this person a producer?",
        "writer": "Is this person a writer or author?",
        "voice_actor": "Is this person a dubbing or voice artist?",
        "comedian": "Is this person a comedian or known for humor?",
        "international":"IS this person international?",
        "host": "Is this person a host or presenter?",
        "singer": "Is this person a singer or musician?",
        "dancer": "Is this person a dancer?",
        "classic_dancer": "Is this person a classic dancer?",
        "classic_icon":"Is this person a classic icon?",
        "classic_star":"Is this person a classic star?",
        "standup_comedian": "Is this person a stand-up comedian?",

        # YouTube & Social Media
        "youtuber": "Is this person a YouTuber?",
        "roaster": "Is this person known for roasting videos?",
        "streamer": "Does this person do live streaming?",
        "gamer": "Is this person a gamer or eSports player?",
        "fashion_influencer": "Is this person a fashion influencer?",
        "spiritual_influencer": "Is this person a spiritual influencer?",
        "content_creator": "Is this person a digital content creator?",
        "vlogger": "Does this person make vlogs or lifestyle videos?",

        # Sports
        "cricketer": "Is this person a cricketer?",
        "footballer": "Is this person a football player?",
        "athlete": "Is this person an athlete?",
        "tennis_player": "Is this person a tennis player?",
        "badminton_player": "Is this person a badminton player?",
        "chess_player": "Is this person a chess player?",
        "coach": "Is this person a coach or mentor?",
        "olympic_medalist": "Has this person won an Olympic medal?",
        "world_champion": "Is this person a world champion?",

        # Business / Technology
        "businessman": "Is this person a businessman or entrepreneur?",
        "entrepreneur": "Is this person an entrepreneur or startup founder?",
        "industrialist": "Is this person an industrialist?",
        "tech_innovator": "Is this person known for innovation in technology?",
        "scientist": "Is this person a scientist or researcher?",
        "philanthropist": "Is this person a philanthropist?",
        "inventor": "Is this person an inventor or technologist?",

        # Political / Historical
        "politician": "Is this person a politician?",
        "leader": "Is this person a leader or ruler?",
        "freedom_fighter": "Was this person a freedom fighter?",
        "historical": "Is this person a historical figure?",
        "revolutionary": "Was this person a revolutionary?",
        "martyr": "Was this person a martyr?",
        "warrior": "Was this person a warrior?",
        "king": "Was this person a king or emperor?",
        "queen": "Was this person a queen or empress?",
        "teacher": "Was this person a teacher or scholar?",
        "philosopher": "Is this person a philosopher or thinker?",

        # Mythology & Religion
        "god": "Is this person a god?",
        "goddess": "Is this person a goddess?",
        "deity": "Is this person a Hindu deity?",
        "mythological": "Is this a mythological character?",
        "epic_character": "Is this character from Mahabharata or Ramayana?",
        "spiritual_leader": "Is this person a spiritual or religious leader?",
        "sage": "Was this person a sage or saint?",

        # Traits / Fame
        "awardee": "Has this person won awards?",
        "international": "Is this person from foreign country?",
        "young_star": "Is this person a young star?",
        "inspirational": "Is this person inspirational or motivational?",
        "romantic_roles": "Is this person known for romantic roles?",
        "action_roles": "Is this person known for action roles?",
        "dramatic_roles": "Is this person known for dramatic performances?",
        "superhero": "Has this person played a superhero?",
        "villain": "Is this person known for villain roles?",
        "comic_roles": "Is this person known for comic roles?",
        "funny": "Is this person funny or humorous?",

        
        "cartoon_network": "Is this character from Cartoon Network?",
        "disney": "Is this character from Disney?",
        "disney_xd": "Is this character from Disney XD?",
        "nickelodeon": "Is this character from Nickelodeon?",
        "netflix": "Is this character from Netflix?",
        "pogo": "Is this character from Pogo TV?",
        "hungama": "Is this character from Hungama TV?"

    }


def make_question(attr, gender=None):
    """
    Dynamically generates smart, gender-sensitive and mythology-aware questions.
    Example:
      make_question('actor', 'male')   -> 'Is he a Bollywood actor?'
      make_question('goddess', 'female') -> 'Is she a Hindu goddess?'
    """
    questions = get_questions()

    # Gender-sensitive phrasing
    pronoun = None
    if gender == "male":
        pronoun = "he"
    elif gender == "female":
        pronoun = "she"

    # Mythology special cases
    if attr in ["god", "goddess", "deity"]:
        if gender == "female":
            return "Is she a Hindu goddess?"
        elif gender == "male":
            return "Is he a Hindu god?"
        else:
            return "Is this person a Hindu god or goddess?"

    if attr == "epic_character":
        return "Is this character from the Mahabharata or Ramayana?"

    # Gender-smart roles
    gender_specific = {
        "actor": f"Is {pronoun or 'this person'} a Bollywood actor?",
        "actress": f"Is {pronoun or 'this person'} a Bollywood actress?",
        "singer": f"Is {pronoun or 'this person'} a singer?",
        "dancer": f"Is {pronoun or 'this person'} a dancer?",
        "comedian": f"Is {pronoun or 'this person'} a comedian?",
        "cricketer": f"Is {pronoun or 'this person'} a cricketer?",
        "politician": f"Is {pronoun or 'this person'} a politician?",
        "influencer": f"Is {pronoun or 'this person'} a social media influencer?",
        "youtuber": f"Is {pronoun or 'this person'} a YouTuber?",
    }

    if attr in gender_specific:
        return gender_specific[attr]

    # Default: return mapped question or fallback
    return questions.get(attr, f"Is {pronoun or 'this person'} known for '{attr}'?")
