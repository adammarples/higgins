from dataclasses import dataclass

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@dataclass
class Person:
    name: str

    @property
    def first_name(self):
        return self.name.split()[0].title()

    @property
    def last_name(self):
        return self.name.split()[1].title()


@app.route('/bot', methods=['POST'])
def bot():
    message = request.values.get('Body', '').lower()
    name = request.values.get('ProfileName', '').lower()
    person = Person(name)
    resp = MessagingResponse()
    msg = resp.message()
    reply = higgins(message, person)
    if reply:
        msg.body(reply)
        return str(resp)
    return ''


def higgins(message: str, person: Person) -> str:
    H = '🤵🏻‍♂️'
    D = '🍸'
    N = 2
    message = message.lower()
    if not message.startswith('higgins'):
        return ''
    if 'drink' in message and 'drinks' not in message:
        N = 1
        noun = 'drink'
    elif 'drinks' in message:
        noun = 'drinks'
    else:
        return ''
    drinks = f'{H}️ Your {noun}, Mr. {person.last_name} Sir {D*N}'
    return drinks



if __name__ == '__main__':
    app.run(debug=True)