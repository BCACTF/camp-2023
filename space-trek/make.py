encoded = '''   		   	 
	
     		   		
	
     		    	
	
     		   		
	
     			 	  
	
     		  		 
	
     				 		
	
      		 	 	
	
     		 	   
	
      		    
	
     	  				
	
     			 	  
	
     	 					
	
     		  		 
	
      		    
	
     	 	  	 
	
     	 					
	
     	 	 	  
	
     		 	   
	
      		  		
	
     	 					
	
      		 	 	
	
     			 	  
	
     	      
	
     			  	 
	
     			  		
	
     	 					
	
      		 			
	
      		   	
	
      		  	 
	
      			   
	
      			  	
	
      		 	  
	
     					 	
	'''.split('\n')

final = ''''''

f = open('mission.txt').readlines()

i = 0
j = 0

while i < len(f) and j < len(encoded):
    final += f[i] + encoded[j] + '\n' + encoded[j+1] + '\n'
    i += 1
    j += 2

final += 'CMP: 1:50.\n  '

f = open('mission_logs.txt', 'w')
f.write(final)
f.close()