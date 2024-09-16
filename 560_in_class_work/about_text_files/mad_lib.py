# Mad lib example for functions

def madlib(adverb_1, noun_1, noun_2, noun_3,adverb_2):
    '''Mad lib function'''
    
    story = f'''
    Ahoy, matey! If ye be wantin' to talk like a true pirate, ye need to master 
    some key phrases. First off, always speak with a hearty.{adverb_1} tone and 
    make sure to use piratey {noun_1} like "ahoy" and "arr." When ye be on the 
    high seas, don't forget to mention yen {noun_2} and keep an eye out for 
    {noun_3}.A true pirate be always{adverb_2}prepared for any swashbuckling 
    adventure!
'''
    return story

 output_story = madlib('slowly', 'cat', 'orange', 'iguana','smelly') 
 print(output_story)