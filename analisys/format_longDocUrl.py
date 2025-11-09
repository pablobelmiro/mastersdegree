import json

question_types = {}
evidence_sources = {}
answer_formats = {}
tasks_tag = {}
count = 0
with open("LongDocURL_public.jsonl", "r", encoding="utf-8", errors="replace") as file:
    for line in file:
        count += 1
        
        try:
            data = json.loads(line)
            #print(data)

            type = data['question_type']
            dict_question = question_types.keys()
            if type in dict_question:
                question_types[type] = question_types[type] + 1
            else:
                question_types[type] = 1

            evidence_src = data['evidence_sources']
            #print(f'evidence_src: {evidence_src}')
            
            for ev in evidence_src:
                if ev is not None or ev != " ":
                    #print(f"ev: {ev}")
                    if ev in evidence_sources:
                        evidence_sources[ev] = evidence_sources[ev] + 1
                    else:
                        evidence_sources[ev] = 1

            answr_format = data['answer_format']
            dict_answer_formats = answer_formats.keys()
            if answr_format in dict_answer_formats:
                answer_formats[answr_format] = answer_formats[answr_format] + 1
            else:
                answer_formats[answr_format] = 1

            task_tag = data['task_tag']
            dict_task_tag = tasks_tag.keys()
            if task_tag in dict_task_tag:
                tasks_tag[task_tag] = tasks_tag[task_tag] + 1
            else:
                tasks_tag[task_tag] = 1
                
            print(f"linha: {count}")
        except:
            print("linha com erro de conversão ou leitura: ", count)
            
            
        
print(f"question_types: {question_types}")
print(f"evidence_sources: {evidence_sources}")
print(f"answer_formats: {answer_formats}")
print(f"tasks_tag: {tasks_tag}")
print(count)