from fastapi import FastAPI, UploadFile, File
import shutil

app = FastAPI()

@app.post('/')
async def upload_file(file: UploadFile = File(...)):
    # with open(f'./data_get/{file.filename}', 'wb') as buffer:
    #     shutil.copyfileobj(file.file, buffer)

    try:
        contents = file.file.read()
        with open(f"./data_get/{file.filename}", 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {'filename': file.filename}
