from flask import Flask, request

# Create a Flask server instance
server = Flask(__name__)

port = 8080

# #step1 -Create a Router
@server.route('/', methods=['GET'])
def audioSummary():
    print(' :::')
    return {"Start" : "First"}


@server.route('/init', methods=['GET'])
def initLoad():
    print('initLoad :::')
    return {"Test" : "Init"}


@server.route('/audio', methods=['GET'])
def audioSummary():
    print('audioSummary :::')
    return {"Test" : "Audio Summary"}

# # Run the Flask server
if __name__ == '__main__':
    server.run(host='0.0.0.0', port=port)


# from wsgiref.simple_server import make_server
# from pyramid.config import Configurator
# from pyramid.response import Response
# import os
# # import whisper
# import torch
# from transformers import pipeline

# def hello_world(request):
#     name = 'Mani'
#     if name == None or len(name) == 0:
#         name = "world"
#     message = "Hello, " + name + "!\n"
#     return Response(message)

# def audio_summary_fun(request):
#     # model = whisper.load_model("base")
#     # audioURL = "https://kesav-dev-dev-ed.file.force.com/sfc/dist/version/download/?oid=00D2w000008WU8p&ids=0682w00000VnlqQ&d=%2Fa%2F2w000000JRd5%2F_uvHKhdl4zvajmOG7wZi.aNSZp5l2rkeSvt2PcV_Qfk&asPdf=false"
#     # result = model.transcribe(audioURL)
#     # res = result["text"]
#     # print('res ::::', res)
#     # return Response(res)


#     device = "cuda:0" if torch.cuda.is_available() else "cpu"
#     transcribe = pipeline(task="automatic-speech-recognition", model="vasista22/whisper-tamil-medium", chunk_length_s=1, device=device)
#     transcribe.model.config.forced_decoder_ids = transcribe.tokenizer.get_decoder_prompt_ids(language="ta", task="transcribe")
#     audioURL = "https://kesav-dev-dev-ed.file.force.com/sfc/dist/version/download/?oid=00D2w000008WU8p&ids=0682w00000VnlqQ&d=%2Fa%2F2w000000JRd5%2F_uvHKhdl4zvajmOG7wZi.aNSZp5l2rkeSvt2PcV_Qfk&asPdf=false"
#     res = transcribe(audioURL)["text"]
#     print('Transcription: ', res)
#     return Response(res)


# if __name__ == '__main__':
#     port = 8080
#     with Configurator() as config:
#         print('Runing')
#         config.add_route('hello', '/')
#         config.add_view(hello_world, route_name='hello')
#         config.add_route('audio_summary', 'audiosummary')
#         config.add_view(audio_summary_fun, route_name='audio_summary')
#         app = config.make_wsgi_app()
#     server = make_server('0.0.0.0', port, app)
#     print('server::::', server)
#     server.serve_forever()