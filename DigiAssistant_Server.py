from google.protobuf.json_format import MessageToJson
import json




def detect_intent_texts(project_id, session_id, texts, language_code):
                import dialogflow_v2 as dialogflow
                session_client = dialogflow.SessionsClient()

                session = session_client.session_path(project_id, session_id)
                print('Session path: {}\n'.format(session))
                text_input = dialogflow.types.TextInput(text=texts, language_code=language_code)
                print('text_input:')
                print(text_input)
                query_input = dialogflow.types.QueryInput(text=text_input)
                print('query_input:')
                print(query_input)
                response = session_client.detect_intent(session=session, query_input=query_input)
                print('response:')
                print(response)
                jsonObj = MessageToJson(response)
                return jsonObj
               



