import requests
import json

AMOUNT = 10
TYPE = "boolean"

respons = requests.get(url=f"https://opentdb.com/api.php?amount={AMOUNT}&type={TYPE}")
respons_jons = respons.json()
# print(respons_jons)
# print(respons_jons['results'][0])
# print(respons_jons['results'][0]['question'])
# print(respons_jons['results'][0]['correct_answer'])

data = {}
data['text'] = respons_jons['results'][0]['question']
data["answer"] = respons_jons['results'][0]['correct_answer']
json_data = json.dumps(data)
# print(json_data)


question_answer = {}
question_data = []
for key in respons_jons['results']:
    # print(key['question'])
    question_answer['text'] = key['question']
    question_answer['answer'] = key['correct_answer']
    question_data.append(question_answer)


# print(question_data)
# question_json_data = json.dumps(question_data)
# print(question_json_data)


# question_data = [
#     {"text": "A slug's blood is green.", "answer": "True"},
#     {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#     {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
#     {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
#     {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, "
#              "you are free to take it home to eat.", "answer": "True"},
#     {"text": "In London, UK, if you happen to die in the House of Parliament, "
#              "you are entitled to a state funeral.", "answer": "False"},
#     {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#     {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
#     {"text": "Google was originally called 'Backrub'.", "answer": "True"},
#     {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
#     {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
#     {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]
