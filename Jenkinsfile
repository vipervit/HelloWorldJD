pipeline {

  agent any

    stages {

      stage('Docker: Make image') {
        steps('remove old and build new image')     {
          sh 'docker rmi tesqos/demojd:latest --force'
          sh 'docker build -t tesqos/demojd:latest .'
        }
      }

      stage('Docker: Push image') {
        steps('push image') {
          sh 'docker push tesqos/demojd:latest'
        }
      }

      stage('pip: Make package') {
        steps('clean up dist, remove old and make new version')  {
          sh 'rm -r -f dist'
          sh 'echo y | pip uninstall demojd'
          sh 'python setup.py sdist'
        }
      }

      stage('pip: Upload package to PyPI') {
        steps('upload package') {
          sh 'python3 -m twine upload dist/* -u vipervit'
        }
      }

      stage('pip: Install new package version in PROD') {
        steps('install package') {
          sh 'source $PROG/python/prod/bin/activate'
          sh 'pip install --upgrade demojd'
        }
      }

    }

}
