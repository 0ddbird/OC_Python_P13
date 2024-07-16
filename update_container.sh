sudo docker pull ${{ secrets.DOCKER_USERNAME }}/mydjangoapp:${{ github.sha }}
sudo docker stop mydjangoapp || true
sudo docker rm mydjangoapp || true
sudo docker run -d --name mydjangoapp -p 8000:8000 ${{ secrets.DOCKER_USERNAME }}/mydjangoapp:${{ github.sha }}
