import whisper

model = whisper.load_model("base")
audioURL = "https://kesav-dev-dev-ed.file.force.com/sfc/dist/version/download/?oid=00D2w000008WU8p&ids=0682w00000VnlqQ&d=%2Fa%2F2w000000JRd5%2F_uvHKhdl4zvajmOG7wZi.aNSZp5l2rkeSvt2PcV_Qfk&asPdf=false"
result = model.transcribe(audioURL)

print('result :::',result["text"] )