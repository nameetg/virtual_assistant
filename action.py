import text_to_speech
import speech_to_text
import datetime
import weather
import webbrowser

def Action(data):
  user_data = data.lower()

  if 'what is your name' in user_data:
    text_to_speech.text_to_speech('my name is virtual assistant')
    return 'my name is virtual assistant'
  
  elif 'hello' in user_data or 'hey' in user_data or 'hi' in user_data:
    text_to_speech.text_to_speech('hello user, how can i help you')
    return 'hello user, how can i help you'
  
  elif 'good morning' in user_data:
    text_to_speech.text_to_speech('good morning!')
    return 'good morning!'
  elif 'time now' in user_data:
    current_time = datetime.datetime.now()
    Time = (str)(current_time)+'hour : ', (str)(current_time.minute) + 'minute'
    text_to_speech.text_to_speech(Time)
    return Time
  
  elif 'shutdown' in user_data:
    text_to_speech.text_to_speech('sure!')
    return 'sure!'
  elif 'play music' in user_data:
    webbrowser.open('https://open.spotify.com/')
    text_to_speech.text_to_speech('opened spotify')
    return 'opened spotify'
  
  elif 'open youtube' in user_data:
    webbrowser.open('https://youtube.com')
    text_to_speech.text_to_speech('opened youtube')
    return 'opened youtube'
  
  elif 'open google' in user_data:
    webbrowser.open('https://google.com')
    text_to_speech.text_to_speech('opened google')
    return 'opened google'

  elif 'weather' in user_data:
    ans = weather.weather()
    text_to_speech.text_to_speech(ans)
    return ans
  else :
    text_to_speech.text_to_speech('this feature is not available as of now')
    return 'this feature is not available as of now'