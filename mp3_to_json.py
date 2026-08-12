import whisper
import json
import os 

model = whisper.load_model("large-v2")

audios=os.listdir("audios")
for audio in audios:
    if "sample1.mp3" not in audio:
        number = audio.split("_")[0]
        title=audio[:-4]
        if "_" in title:
            title = title.replace(f"{number}_","",1)
        print(number,title)
        result = model.transcribe(audio = f"audios/{audio}",
                            language ="hi",
                            task="translate",
                            word_timestamps=False)

        # print(result["segments"],"\n\n\n")
        chunks=[]
        for segment in result["segments"]:
            chunks.append({"number":number , "title":title, "id":segment["id"], "start":segment["start"], "end":segment["end"] ,"text":segment["text"]})
        # print(chunks)
        chunks_meta_data={"chunk": chunks,"text":result["text"]}

        with open(f"output_json/{audio}.json","w") as f:
            json.dump(chunks_meta_data,f) 