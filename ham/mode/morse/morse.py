class morse(object):    
    def __init__(self):
        self.alpha={'a':'.-',
       'b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..',
       'm':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--',
       'x':'-..-','y':'-.--','z':'--..'}
        #A Hash is 3 times longer than a dot
        #The gap between letters is 3 times that of a dot
        #The Gap between Words is 7 times that of a dot.
        #Note in the code I have added only 4 for the space as I added 3 already for the char.
        for k in self.alpha.keys():
            self.alpha[k]=' '.join([c for c in self.alpha[k]]).replace('-','---')
        self.word_gap=' '

    def text_to_elements(self,Text='paris '*5):    
        output=''
        for c in Text:
            if c in self.alpha:
                output=output+self.alpha[c]+'0'*3
            else:
                if c==self.word_gap:
                    output=output+'0'*4        
        output=output.replace('.','1').replace('-','1').replace(' ','0')        
        return output
    #5WPM sends 'paris ' 5 times in 250 elements
    
    def calc_elements_per_wpm(self,wanted_wpm):
        #5WPM is defined as 'paris ' sent 5 times in 1 minute
        #'paris '*5 has 250 elements 
        # so per milli second 5 wpm means each element is multiplied by 19.4 (rounded to 20)
        scale = int(20.0*(5.0/wanted_wpm))
        return scale
    
    
    #250 elements per minute means each element (as  5 WPM - i.e. Paris (50 Elements)) takes 60/250 
    #20 Milli Second per element  or 5.2 elements per second 
    #Output needs to be scaled
    #say expanded by 20 so each element is a milli second

    def expand(self,data,scale):
        newoutput=''
        for c in data:
            newoutput=newoutput+c*scale
        return newoutput
        
        
    def pad_to(self,elements,pad_length=5000):
        #we need to make sure that the output data array is a consistent size
        if len(elements)>pad_length:
            return elements[:pad_length]
        else:
            to_add=pad_length-len(elements)
            return elements+'0'*to_add


if __name__=="__main__":
	cw=morse()
	elements=cw.text_to_elements('tim')
	#
	sf=cw.calc_elements_per_wpm(5)
	scale=cw.calc_elements_per_wpm(5)
	fivewpm=cw.expand(elements,scale)
	paddedfivewpm=cw.pad_to(fivewpm,1000)
	paddedfivewpm[:200]
