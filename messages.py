import random


def subject_selector():

    subject_options =[
        "[Fund11] Cast Your Vote for Cardano's Future!",
        "[Fund11] Elevate Cardano!",
        "Your Vote Matters! Discover Top-Rated Proposals.",
        "Explore Community-Backed Fund11 Proposals!",
        "[Fund11] Shape the Destiny of Cardano!",
        "Support High-Rated Fund11 Proposals!",
        "[Fund11] Vote for Success!",
        "Vote for Standout Fund11 Proposals!",
        "Explore Community-Prized Fund11 Proposals!",
    ]
    return random.choice(subject_options)

def body_selector():

    intro =[
        "Vote for Excellence!<br>Explore our Developers category proposals!<br><br>Why us?",
        "Elevate Cardano with Us!<br>Discover our Developers category proposals impact!<br><br>Why choose us?",
        "Unleash the potential of our Developers category proposals!<br><br>Why support us?",
        "Revolutionize with Developers!<br>Your vote matters in the Developers category!<br><br>Why us?",
        "Discover our Developers category proposals!<br><br>Why support us?",
        "Explore the Developers category!<br><br>Why choose us?",
        "Your voice matters in the Developers category!<br><br>Why support us?",
        "Discover our Developers category proposals!<br><br>Why choose us?",
        "Developers Unite for Cardano!<br>Unleash the potential of our Developers category proposals!<br><br>Why support us?",
        "Your Vote Powers Progress!<br>Explore our Developers category proposals!<br><br>Why us?",
        "Your Vote, Your Cardano Legacy!<br>Discover our Developers category proposals!<br><br>Why support us?",
        "Your voice matters in the Developers category!<br><br>Why us?"
        ]
    success = [
        "* Unmatched Success: 100K+ app downloads.",
        "* Stellar Track Record: 100K+ app downloads.",
        "* Proven Success: App triumph with 100K+ downloads.",
        "* Proven Excellence: App with 100K+ downloads.",
        "* Unparalleled Success: App soaring with 100K+ downloads.",
        "* Track Record: App triumph with 100K+ downloads.",
        "* App Success: Soaring with 100K+ downloads.",
        "* Unmatched Success: 100K+ app downloads.",
        "* Proven Success: App soaring with 100K+ downloads.",
        "* Unmatched Success: 100K+ app downloads.",
        "* Unparalleled Success: App soaring with 100K+ downloads.",
        "* App Success: Soaring with 100K+ downloads."        ]
    collaboration = [   
        "* Trusted Partner: Microsoft for Startups Founders Hub.",
        "* Power of Collaboration: Microsoft for Startups Founders Hub.",
        "* Collaborative Power: Microsoft for Startups Founders Hub alliance.",
        "* Strategic Collaborator: Microsoft for Startups Founders Hub.",
        "* Collaboration Dynamo: Partnered with Microsoft for Startups Founders Hub.",
        "* Trusted Partner: Microsoft for Startups Founders Hub.",
        "* Collaboration Dynamo: Microsoft for Startups Founders Hub ally.",
        "* Trusted Collaborator: Microsoft for Startups Founders Hub.",
        "* Collaborative Dynamo: Partnered with Microsoft for Startups Founders Hub.",
        "* Trusted Collaborator: Microsoft for Startups Founders Hub.",
        "* Collaboration Dynamo: Partnered with Microsoft for Startups Founders Hub.",
        "* Collaboration Dynamo: Microsoft for Startups Founders Hub ally."        ]
    experts = [        
        "* Blockchain Mastery: Deep Cardano expertise.",
        "* Blockchain Experts: Proficient in Cardano tech.",
        "* Blockchain Prowess: Cardano tech expertise.",
        "* Blockchain Gurus: Experts in Cardano tech.",
        "* Blockchain Whizzes: Mastery in Cardano tech.",
        "* Blockchain Mastery: Deep Cardano expertise.",
        "* Blockchain Gurus: Experts in Cardano tech.",
        "* Blockchain Prowess: Deep Cardano expertise.",
        "* Blockchain Mastery: Experts in Cardano tech.",
        "* Blockchain Prowess: Deep Cardano expertise.",
        "* Blockchain Whizzes: Mastery in Cardano tech.",
        "* Blockchain Gurus: Experts in Cardano tech."        ]
    ratting = [
        "* Highly Rated: Community feedback supports our proposals!",
        "* Community Choice: Our proposal received great reviews!",
        "* Standout Performer: Our proposals earned high community ratings!",
        "* Highly Acclaimed: Our proposals received top community ratings",
        "* Community-Endorsed: Our proposals stands out with high ratings!",
        "* Rated High: Our proposals earned praise during the community review stage!",
        "* Ratings: Our proposals stood out during community review!",
        "* Backed by the Community: Our proposals received high ratings in the review stage!",
        "* Community Endorsement: Our proposals earned praise with outstanding reviews!",
        "* Resonating Success: Our proposal received top reviews during the community stage!",
        "* Recognized Excellence: Our proposal earned high community ratings during review!",
        "* Community-Praised: Our proposal is a standout performer with high ratings!"
    ]    
    revolution = [
        "* Focus: DevTools for 45%+ global websites.",
        "* Revolution: DevTools for 45%+ global websites.",
        "* Integration: DevTools for 45%+ global websites.",
        "* Evolution: DevTools for 45%+ global websites.",
        "* Transformation: DevTools for 45%+ global websites.",
        "* Revolution: DevTools for 45%+ global websites.",
        "* Evolution: DevTools for 45%+ global websites.",
        "* Focus: DevTools for 45%+ global websites.",
        "* Evolution: DevTools for 45%+ global websites.",
        "* Focus: DevTools for 45%+ global websites.",
        "* Transformation: DevTools for 45%+ global websites.",
        "* Evolution: DevTools for 45%+ global websites."
    ]    
    signature = [
        '''Search "Esubalew" to locate our proposals quickly. Cast your vote and propel Cardano forward!''',
        '''Search "Esubalew" - Your vote is the catalyst! Easily find our proposals and ignite Cardano's progress!''',
        '''Your Vote, Your Impact! Search "Esubalew" - Locate our proposals easily and cast a vote that transforms Cardano!''',
        '''Navigate Change - Search "Esubalew" - Find our proposals with a simple search. Your vote steers Cardano's course!''',
        '''Easy Access, Big Impact! Search "Esubalew" - Discover our proposals effortlessly. Your vote shapes the destiny of Cardano!''',
        '''Search "Esubalew" to locate our proposals quickly. Cast your vote and propel Cardano forward!''',
        '''Search "Esubalew" - Explore our proposals with ease. Your vote is the catalyst for Cardano's growth!''',
        '''Search "Esubalew" - Access our proposals effortlessly. Every vote paves the way for a stronger Cardano!''',
        '''Search "Esubalew" - Make your vote count! Find us easily and fuel Cardano's evolution.''',
        '''Search "Esubalew" - Easily access our proposals! Cast your vote for a thriving Cardano.''',
        '''Search "Esubalew" to find our proposals easily. Your vote shapes Cardano's future!''',
        '''Search "Esubalew" for easy access to our proposals. Your vote fuels progress!'''
    ]

    selected_content = (
        random.choice(intro) + '<br>'+
    
    random.choice(success) + '<br>' +
     random.choice(collaboration) + '<br>'+
     random.choice(experts) + '<br>'+
     random.choice(ratting) + '<br>'+
     random.choice(revolution)+ '<br>'

    '<br>'+random.choice(signature)
    )

    return selected_content