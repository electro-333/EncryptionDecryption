
__author__ = """ Badr """
__date__ = """11/4/2021"""
__version__ = """0.0.1"""

from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.picker import MDDatePicker
from kivymd.app import MDApp
import base64
##########################################################


KV = '''
ScreenManager:
	FirstScreen:

		
<FirstScreen>:
	name:"FirstScreen"
	MDFloatLayout:
		md_bg_color:[0/255,0/255,0/255,1]
		MDRaisedButton:
			text:"Encrypt"
			pos_hint:{"center_x":.25,"center_y":.85}
			size_hint:.4,.05
			md_bg_color:[100/255,100/255,100/255,1]
			on_press:app.Encrypt()
		MDRaisedButton:
			text:"Decrypt"
			pos_hint:{"center_x":.75,"center_y":.85}
			size_hint:.4,.05
			md_bg_color:[100/255,100/255,100/255,1]
			on_press:app.Decrypt()
			
		MDTextField:
			mode:"rectangle"
			id:textFile
			size_hint:.84,.2
			multiline:True
			pos_hint : {"center_y":.7,"center_x":.5}
			color_mode:'custom'
			line_color_focus:[255/255,255/255,255/255,1]
			hint_text:"      "
			font_size:20
			hint_text:"encryption      "
			id:enc
		MDTextField:
			mode:"rectangle"
			id:textFile
			size_hint:.84,.2
			multiline:True
			pos_hint : {"center_y":.5,"center_x":.5}
			color_mode:'custom'
			line_color_focus:[255/255,255/255,255/255,1]
			hint_text:"      "
			font_size:20
			hint_text:"decryption      "
			id:dec
		
'''
############################################################
class FirstScreen(Screen):
    pass
    
class ControllScreen(Screen):
    pass
    
class OpenFileScreen(Screen):
    pass
    	
class KeyLoggerScreen(Screen):
    pass
    
class LearnScreen(Screen):
    pass
############################################################
sm = ScreenManager()



sm.add_widget(FirstScreen(name = 'FirstScreen'))



############################################################
class Main(MDApp):

	def build(self):
		
		self.app1=Builder.load_string(KV)
		
		return self.app1
		
	def Encrypt(self):
		
		text = self.app1.get_screen('FirstScreen').ids.enc.text
		
		textEncrypted = base64.b64encode(text.encode())
		
		self.app1.get_screen('FirstScreen').ids.dec.text=f"{textEncrypted.decode()}"
		
		
		
		
	def Decrypt(self):
		
		text = self.app1.get_screen('FirstScreen').ids.dec.text
		
		textEncrypted = base64.b64decode(text)
		
		self.app1.get_screen('FirstScreen').ids.enc.text=f"{textEncrypted.decode()}"
		
##############################################################

		   
		    
		      
Main().run()
