class crier:
	def __init__(self, name, body):
		self.name = name
		self.body = body
		print(self.name)
		print(self.body)

	def shout(self, news):
		self.news = news
		print(self.news)

mycrier = crier("Earl The Crier", """
 #####      
      #### _\_    
      ##=-[.].]   
      #(    _\    
       #  \__|_.--._
     .' \___/       \/;;
    /  .'   `-----\  `/
    (  ).    ,----(   )
     (   )   |'   (   )
     |(   )  |    (   )
     | (  )  |    (   )
     |_|  )=={    (  ))
     :.. )   |     `-'
     ''') Y  |    
      (|  |  |    
       |  |  |    
       |  )  )    
       |  |  |      
       |__|__|_   
       [____)__)  
	""")

mycrier.shout()