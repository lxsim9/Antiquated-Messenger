class pigeon:
	def __init__(self, name, body):
		self.name = name
		self.body = body 
		print(self.name)	 
		print(self.body) 
	
	def send_message(self, message):
		self.message = message 
		print(self.message)
		
mypigeon = pigeon("Chyna", """  
	______ __ 
	{-_-_= '. `'.
	{=_=_-  \   \
	 {_-_   |   /
	  '-.   |  /    .===,
	.--.__\  |_(_,==`  ( o)'-.
	`---.=_ `     ;      `/    \
	  `,-_       ;    .'--') /
	    {=_       ;=~`    `"`
	     `//__,-=~`
	     <<__ \\__
	      /`)))/`)))
""")
mypigeon.send_message()
