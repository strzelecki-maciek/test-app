VER=$(sed -n 's/^VERSION = "\([0-9.]*\)".*/\1/p' app.py)
echo $VER
docker build -t mstrzelecki/app:${VER} .
docker push mstrzelecki/app:${VER}
