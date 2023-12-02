import joblib

#global var

lem=joblib.load('chatbot/chat_bot/lematizer.joblib')
non_standard=joblib.load('chatbot/chat_bot/non_standard.joblib')
standard=joblib.load('chatbot/chat_bot/standard.joblib')
classifier=joblib.load('chatbot/chat_bot/disease_clf_deep.joblib')
symp_finder=joblib.load('chatbot/chat_bot/symptom_finder_final.joblib')
disease=joblib.load('chatbot/chat_bot/disease_list.joblib')
dis_descr=joblib.load('chatbot/chat_bot/dis_descr.joblib')
dis_prec=joblib.load('chatbot/chat_bot/dis_prec.joblib')
def lematize(text):
    #lematize a sentence
    doc=lem(text)
    ans=''
    for i in doc:
        ans+=(i.lemma_ + ' ')
    return ans[:-1]

def find_symptoms(text):
    #finds symptoms in user text
    doc=symp_finder(text)
    symptoms=[]
    for i in doc.ents:
        if i.label_=='SYMPTOM':
            symptoms.append(i)
    if len(symptoms)==0:
        raise Exception('noMatchingSymptoms')
    return symptoms

def convert_to_standard(symptoms):
    #convert detected symptoms to base symptoms
    base_hash=standard
    for i in symptoms:
        x=str(i)
        try:
            base_hash[non_standard[x]]=1
        except Exception:
            try:
                base_hash[x]=1
            except Exception:
                continue
    return base_hash

def find_disease(symptom_array):
    # find the most relatable disease and return it
    inp=[]
    inp.append(list(symptom_array))
    prediction=classifier.predict(inp)
    m=0
    ind=0
    lst=list(prediction[0])
    # print(lst)i am 
    for i in range(len(lst)):
        if lst[i]>m:
            m=lst[i]
            ind=i
    return disease[ind]

def generate_response(disease):
    response='Based on your symptoms you have '
    response+=disease + '\n'
    response+='so basicaly, '
    try:
        response+=dis_descr[disease]+'\n'
        response+='now you must '
        response+=dis_prec[disease]
        return response
    except Exception:
        response+='you must not take this lightly visit the nearest hospital as soon as possible'


# use only this function to generate----->
def chatbot_reply(query):
    query=lematize(query)
    try:
        symptoms=find_symptoms(query)
    except Exception as e:
        raise Exception(e)
    hm=convert_to_standard(symptoms)
    lst=list(hm.values())[:-1]
    disease=find_disease(lst)
    return generate_response(disease)


# if __name__=='__main__':
#     query=input('Enter query:')
#     query=lematize(query)
#     symptoms=find_symptoms(query)
#     hm=convert_to_standard(symptoms)
#     lst=list(hm.values())[:-1]
#     disease=find_disease(lst)
#     print(generate_response(disease))


