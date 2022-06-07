# onlineauthenticator
Source code repo of onlineauthenticator.com

## run test develop local
setup venv
`python -m venv venv`

activate venv
`source venv/bin/activate`

install packages
`pip install -r requirements.txt`

run local 
`uvicorn app.main:app --host 0.0.0.0 --port 80`
