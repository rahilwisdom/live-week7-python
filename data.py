user_data = {
    "Shandy": ["Basic Plan", 13, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Standard Plan", 24, "ana-2f9g"],
    "Bagus": ["Basic Plan", 24, "bagus-9f92"]
}

header = ['Basic Plan', 'Standard Plan', 'Premium Plan', 'Services']
table = [[True, True, True, 'can_stream'],
         [True, True, True, 'can_download'],
         [True, True, True, 'has_SD'],
         [False, True, True, 'has_HD'],
         [False, False, True, 'has_UHD'],
         [1, 2, 4, 'num_of_devices'],
         ['3rd party movie only', 
          'Basic Plan Content + Sports (F1, Football, Basketball)',	
          'Basic Plan + Standard Plan + PacFlix Original Series or Movie', 'content'],
         [120_000, 160_000, 200_000, 'price']]