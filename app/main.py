from fastapi import FastAPI
import py_eureka_client.eureka_client as eureka_client
import uvicorn

rest_port = 29913
eureka_server_name = 'http://localhost:8761/eureka'
app_name = 'kimchi-ai-app-service'
eureka_client.init(
    eureka_server=eureka_server_name,
    app_name=app_name,
    instance_port=rest_port
)

app = FastAPI()

@app.get('/ai/intro')
def hello():
    return {'msg':'hello fastapi'}

if __name__ == '__main__':
    print("server starting...")
    uvicorn.run(app=app, host='0.0.0.0',port=rest_port)