# Customized from donnemartin/data-science-ipython-notebooks
# Original: https://github.com/donnemartin/data-science-ipython-notebooks
# Cloned on: 2025-07-14

import re


class TransformUtil:

    @classmethod
    def remove_punctuation(cls, value):
        """Removes !, #, and ?.
        """        
        return re.sub('[!#?]', '', value) 

    @classmethod
    def clean_strings(cls, strings, ops): 
        """General purpose method to clean strings.

        Pass in a sequence of strings and the operations to perform.
        """        
        result = [] 
        for value in strings: 
            for function in ops: 
                value = function(value) 
            result.append(value) 
        return result