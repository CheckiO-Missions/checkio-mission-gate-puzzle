"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": "Speak friend and enter.",
            "answer": "friend",
            "explanation": {'friend': 31.259071428571428, 'enter': 30.758601190476192, 'speak': 30.756839285714285,
                            'and': 27.75797619047619},
        },
        {
            "input": "Beard and Bread",
            "answer": "bread",
            "explanation": {'beard': 42.68222222222222, 'bread': 42.68222222222222, 'and': 35.34444444444444},
        },
        {
            "input": "The Doors of Durin, Lord of Moria. Speak friend and enter. I Narvi made them. Celebrimbor of Hollin drew these signs",
            "answer": "these",
            "explanation": {'i': 10.274957431457432, 'made': 24.309076891362604, 'hollin': 21.497629698343985,
                            'the': 22.012223768295197, 'them': 23.832666838452553, 'friend': 21.97526736755308,
                            'celebrimbor': 13.380944925444926, 'speak': 24.175910362124647, 'and': 21.059719233147806,
                            'these': 25.605414931629216, 'drew': 23.83304401154401, 'doors': 25.129986703772417,
                            'signs': 24.652487116058545, 'enter': 24.17764883529169, 'lord': 23.83333879612451,
                            'of': 18.406394832680547, 'durin': 25.13008276643991, 'narvi': 24.177331443688587,
                            'moria': 24.17783288669003},
        },
        {
            "input": "Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy. According to a researcher at Cambridge University.",
            "answer": "according",
            "explanation": {'researcher': 20.577702535559677, 'to': 17.19488888888889, 'at': 20.05415419501134,
                            'aoccdrnig': 24.38775149453721, 'according': 24.38775149453721,
                            'cambridge': 21.530438672438674, 'a': 16.100674603174603, 'uinervtisy': 21.291040816326532,
                            'university': 21.291040816326532, 'cmabrigde': 21.530438672438674,
                            'rscheearch': 20.577702535559677},
        },
        {
            "input": "One, two, two, three, three, three.",
            "answer": "three",
            "explanation": {'one': 32.339666666666666, 'three': 39.01166666666666, 'two': 35.675666666666665},
        },
    ],
    "Extra": [
        {
            "input": "All that is gold does not glitter,",
            "answer": "gold",
            "explanation": {'all': 25.76985714285714, 'is': 21.94261224489796, 'gold': 28.168836734693876,
                            'not': 27.198615646258503, 'does': 28.168439909297053, 'that': 28.167765306122448,
                            'glitter': 20.82174603174603},
        },
        {
            "input": "Not all those who wander are lost;",
            "answer": "are",
            "explanation": {'all': 29.36169387755102, 'not': 29.36302380952381, 'those': 25.864027210884355,
                            'lost': 27.720761904761904, 'are': 30.791122448979593, 'wander': 23.57712244897959,
                            'who': 29.362357142857142},
        },
        {
            "input": "The old that is strong does not wither,",
            "answer": "that",
            "explanation": {'is': 21.253714285714285, 'not': 26.880979166666666, 'strong': 21.88116964285714,
                            'wither': 21.880911706349206, 'does': 26.568236111111112, 'that': 27.817776785714287,
                            'old': 25.6293125, 'the': 26.881229166666667},
        },
        {
            "input": "Deep roots are not reached by the frost.",
            "answer": "are",
            "explanation": {'reached': 20.89856349206349, 'not': 26.42447619047619, 'roots': 25.18518253968254,
                            'are': 26.425166666666666, 'by': 19.69892857142857, 'deep': 24.70957142857143,
                            'frost': 25.18486904761905, 'the': 26.425130952380954},
        },
        {
            "input": "From the ashes a fire shall be woken,",
            "answer": "fire",
            "explanation": {'woken': 24.25421130952381, 'a': 14.75375, 'be': 21.379541666666668,
                            'ashes': 25.506794642857145, 'from': 25.878645833333334, 'shall': 24.255041666666667,
                            'fire': 28.379919642857143, 'the': 24.880315476190475},
        },
        {
            "input": "A light from the shadows shall spring;",
            "answer": "shall",
            "explanation": {'spring': 26.534998969284683, 'light': 24.923913832199545, 'a': 12.687721088435374,
                            'shadows': 24.69965543186972, 'from': 23.595328798185943, 'shall': 27.78191609977324,
                            'the': 20.91280612244898},
        },
        {
            "input": "Renewed shall be blade that was broken,",
            "answer": "blade",
            "explanation": {'blade': 30.06820634920635, 'broken': 27.250413832199545, 'be': 22.515632653061225,
                            'shall': 25.781469387755102, 'that': 24.668244897959184, 'renewed': 22.454506802721088,
                            'was': 22.34212244897959},
        },
        {
            "input": "The crownless again shall be king.",
            "answer": "again",
            "explanation": {'crownless': 18.894198653198654, 'again': 25.117223665223666, 'be': 20.948981481481482,
                            'king': 24.81119191919192, 'shall': 25.116142857142858, 'the': 24.755055555555554},
        },
        {
            "input": "I don't know half of you half as well as I should like; and I like less than half of you half as well as you deserve.",
            "answer": "half",
            "explanation": {'don': 22.33675170068027, 'should': 16.457886904761907, 'as': 22.274557823129253,
                            'you': 23.05143537414966, 'of': 21.55908163265306, 'i': 14.709132653061225,
                            't': 13.63609693877551, 'like': 23.562173752834468, 'and': 23.408470238095237,
                            'know': 22.132487528344672, 'less': 24.276591836734696, 'deserve': 15.257276077097506,
                            'half': 24.99205612244898, 'well': 22.847531462585035, 'than': 22.847390589569162},
        },
        {
            "input": "Fantasy is escapist, and that is its glory. If a soldier is imprisioned by the enemy, don't we consider it his duty to escape?. If we value the freedom of mind and soul, if we're partisans of liberty, then it's our plain duty to escape, and to take as many people with us as we can!",
            "answer": "the",
            "explanation": {'his': 21.894810074106683, 'take': 22.65262826815369, 'escape': 18.63424408736273,
                            'partisans': 14.14897656956979, 're': 22.195431628635017, 'with': 20.110042177220144,
                            'fantasy': 16.309890975314705, 'our': 21.04611045075452, 'of': 21.347872979186537,
                            'that': 21.46592459706019, 'imprisioned': 12.484625551473009, 'and': 21.894662105314648,
                            'value': 19.604385224003867, 'many': 20.787457993983416, 'a': 12.327319392471935,
                            'it': 22.535768055861276, 'soul': 19.77057191772446, 'people': 18.4639205248612,
                            'mind': 20.279220265610096, 'liberty': 16.139969353621897, 'duty': 20.957000073372956,
                            'as': 22.704882664416562, 'don': 21.21627187125492, 'is': 23.383235099175778,
                            's': 13.344515652897009, 'if': 22.534828184997675, 'its': 23.421275637733263,
                            'escapist': 14.745582299997555, 'we': 22.8736978379436, 'us': 21.856404052632865,
                            'consider': 14.067265194316041, 'can': 21.046630909580063, 'plain': 18.588098503191723,
                            't': 13.514187027661604, 'the': 23.589851248563114, 'soldier': 15.632124306014136,
                            'glory': 18.925840878518844, 'to': 22.02686208330276, 'enemy': 19.43498907965857,
                            'then': 21.296858708146843, 'by': 21.516183579132733, 'freedom': 15.122611086653459},
        },
    ]
}
