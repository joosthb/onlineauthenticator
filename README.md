# onlineauthenticator
Source code repo of onlineauthenticator.com

local build
`podman build -t onlineauthenticator .`

local run
`podman run --rm -p 80:80 onlineauthenticator`