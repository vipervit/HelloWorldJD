pipeline {

  agent any

    stages {

      stage('Docker: Make image') {
        steps('remove image')     { sh 'docker rmi tesqos/demojd:latest --force' }
        steps('build new image')  { sh 'docker build -t tesqos/demojd:latest .' }
      }

      stage('Docker: Push image') {
        steps('push image') { sh 'docker push tesqos/demojd:latest' }
      }

      stage('pip: Make package') {
        steps('clean up dist')      {  sh 'rm -r -f dist' }
        steps('remove old version') { sh 'echo y | pip uninstall demojd' }
        steps('make new version')   {  sh 'python setup.py sdist' }
        }
      }

      stage('pip: Upload package to PyPI') {
        steps('upload package') { sh 'python3 -m twine upload dist/* -u vipervit' }

      stage('pip: Install new package version') {
        steps('install package') { sh 'pip install --upgrade demojd' }
      }

    }

}
