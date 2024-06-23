from flask import Flask, Blueprint,jsonify,redirect,url_for,request

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from sentence_transformers import SentenceTransformer, util
import nltk
import re
import json 
tokenizer_t5 = AutoTokenizer.from_pretrained("potsawee/t5-large-generation-squad-QuestionAnswer")
model_t5 = AutoModelForSeq2SeqLM.from_pretrained("potsawee/t5-large-generation-squad-QuestionAnswer")
model_sentence_transformer = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")



def generate_questions(selected_sentences):
    result=[]
    # Iterate over sentences in groups of 3
    for i in range(0, len(selected_sentences), 2):
        # Get the next 2 sentences for even length, or 3 sentences for odd length
        n = len(selected_sentences)
        if n % 2 == 0:
            context_sentences = selected_sentences[i:i + 2]
        else:
            context_sentences = selected_sentences[i:i + 3]

        # Combine sentences to form context
        context = " ".join(context_sentences)

        question, answer = generate_question(context)
        result.append({"Question": question, "Answer": answer})

    return result
        
def generate_question(context):
    inputs = tokenizer_t5(context, return_tensors="pt")
    outputs = model_t5.generate(**inputs, max_length=100)
    question_answer = tokenizer_t5.decode(outputs[0], skip_special_tokens=False)
    question_answer = question_answer.replace(tokenizer_t5.pad_token, "").replace(tokenizer_t5.eos_token, "")
    question, answer = question_answer.split(tokenizer_t5.sep_token)
    return answer,question

# Example text
text = """ Parallel Processing 
• Parallel processing can be described as a class of techniques which enables the system to 
achieve simultaneous data-processing tasks to increase the computational speed of a 
computer system. 
• A parallel processing system can carry out simultaneous data-processing to achieve faster 
execution time. For instance, while an instruction is being processed in the ALU 
component of the CPU, the next instruction can be read from memory. The primary purpose of parallel processing is to enhance the computer processing 
capability and increase its throughput, i.e. the amount of processing that can be 
accomplished during a given interval of time. 
• A parallel processing system can be achieved by having a multiplicity of functional units 
that perform identical or different operations simultaneously. The data can be distributed 
among various multiple functional units. 
• The following diagram shows one possible way of separating the execution unit into 
eight functional units operating in parallel. 
"""

# Use NLTK for sentence tokenization
sentences = nltk.sent_tokenize(text)

# Function to remove numbers from a sentence
def remove_numbers(sentence):
    return re.sub(r'\d+', '', sentence)

# Remove numbers from each sentence
sentences_without_numbers = [remove_numbers(sentence) for sentence in sentences]

# List to store selected sentences and their scores
selected_sentences_with_scores = []

# List to store chunks of selected sentences
selected_sentences_chunks = []

# Function to score a block of sentences and append two sentences with the highest scores
def score_and_append(sentences_block, text, model, selected_sentences_with_scores):
    # Encode each sentence
    sentence_embeddings = model.encode(sentences_block, convert_to_tensor=True)

    # Print the scores of every sentence in the block
    scores = []
    for idx, sentence_embedding in enumerate(sentence_embeddings):
        similarity_score = util.pytorch_cos_sim(model.encode([text], convert_to_tensor=True), sentence_embedding).item()
        scores.append(round(similarity_score, 3))

    # Find indices of top two sentences with the highest similarity scores
    top_indices = sorted(range(len(sentence_embeddings)), key=lambda i: scores[i], reverse=True)[:2]

    # Append the selected sentences and their scores to the list
    for idx in top_indices:
        selected_sentences_with_scores.append((sentences_block[idx], scores[idx]))

# Iterate over sentences in groups of 3
for i in range(0, len(sentences_without_numbers), 3):
    # Get the next 3 sentences
    selected_sentences_block = sentences_without_numbers[i:i + 3]

    # Call the function to score the block of sentences and append two sentences with scores to the list
    score_and_append(selected_sentences_block, text, model_sentence_transformer, selected_sentences_with_scores)

# Check if there are remaining sentences to create a new chunk
if selected_sentences_with_scores:
    # Append the remaining chunk to the list
    selected_sentences_chunks.append([sentence for sentence, _ in selected_sentences_with_scores])

# Display the final list of selected sentences as a list

selected_sentences = [sentence for sentence, _ in selected_sentences_with_scores]


    
app = Flask(__name__) 
nip=Blueprint("nip",__name__)
# Pass the required route to the decorator. 
@nip.route("/hello") 
def hello(): 
    candy=[]
    for chunk in selected_sentences_chunks:
        
        questions_and_answers = generate_questions(chunk)
        candy.extend(questions_and_answers)

    return jsonify({"questions_and_answers": candy})

if __name__ == "__main__": 
	app.run(debug=True)