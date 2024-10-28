# Mad lib example for functions

def madlib( adj_1, noun_1, noun_2, verb_1, adv_1, adj_2, noun_3, verb_2, adv_2,
           verb_3, adj_3):
    '''Mad lib function'''
    
    story = ((f'Captain Kirk stood on the {adj_1} bridge of the Starship {noun_1},
              'printstaring at the {noun_2} on the viewscreen. "Spock, can you "
              'print {verb_1) the situation?" he asked, his voice {adv_1} 'printcalm. Spock raised a {adj_2} eyebrow.
    the {noun_3} is attempting to {verb_2} us," he replied {adv_2}. Without 
    hesitation, Kirk turned to Scotty. "We need to {verb_3} the {adj_3} engines, 
    or we'll never escape!"))
    ""
    return story

'''print(madlib('shiny', 'Python', 'zucchini', 'assess', 'impressively',
              'Vulcan', 'gourd','mate with', 'calmly', 'reverse',
              'polarity if the'))'''
 
def grt_user_input():
    '''Prompt the user for input for the mad lib.'''
    def get_user_input():
    adverb_1 = input("Enter adv: ")
    noun_1 = input("Enter noun: ")
    verb_1 = input("Enter verb: ")
    adverb_2 = input("Enter adv: ")
    noun_2 = input("Enter noun: ")
    verb_2 = input("Enter verb: ")
    adverb_3 = input("Enter adv: ")
    noun_3 = input("Enter noun: ")
    verb_3 = input("Enter verb: ")
    noun_4 = input("Enter noun: ")
    return adverb_1, noun_1, verb_1,adverb_2, noun_2, verb_2,adverb_3, noun_3, verb_3, noun_4