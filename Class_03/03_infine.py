def exactMatch(text, pat, text_index, pat_index):
	    if text_index == len(text) and pat_index != len(pat):
        	return 0
	   
	      # Else If last character of pattern reaches
	    if pat_index == len(pat):
		        return 1
	   
	    if text[text_index] == pat[pat_index]:
		        return exactMatch(text, pat, text_index + 1, pat_index + 1)
	   
	    return 0
	  
	   

	# This function returns true if 'text' contain 'pat'
	def contains(text, pat, text_index, pat_index):

		      # If last character of text reaches
	    if text_index == len(text):
		        return 0
	   
	      # If current characters of pat and text match
	    if text[text_index] == pat[pat_index]:
	        if exactMatch(text, pat, text_index, pat_index):
	            return 1
         else:
            return contains(text, pat, text_index + 1, pat_index)
	   
	      # If current characters of pat and tex don't match
	    return contains(text, pat, text_index + 1, pat_index)
