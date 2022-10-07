# Created on: 07/10/2022 (GMT+5)
# Created by: Ahmer Aamir

sentence = input("Please enter a string: ")
words = sentence.split()
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
'''
 Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object.
 This enumerated object can then be used directly for loops or converted into a list of tuples using the list() method.
 Example: string "i am ahmer" gives list of tuples [(0, 'i'), (1, 'am'), (2, 'ahmer')]
'''
for i, word in enumerate(words):
    # If the first letter is vowel append "hay" at the end
    if word[0] in vowels:
        words[i] += "hay"
    else:
        '''
        else get vowel position and postfix all the consonants 
        present before that vowel to the end of the word along with "ay"
        '''
        contain_vowels = False
        for j, letters in enumerate(word):
            if letters in vowels:
                words[i] = word[j:] + word[:j] + "ay"
                contain_vowels = True
                break
        # If word contains no vowel letter then simply append "ay" at the end
        if not contain_vowels:
            words[i] += "ay"

# Driver Code
piglatin = ' '.join(words)
print("Pig Latin: ", piglatin)
