pipeline {

  agent any

    stages {
      stage('Deploy in cloud') {
        steps('Make and push docker image') {
          sh 'docker rmi tesqos/demojd:latest --force'
          sh 'docker build -t tesqos/demojd:latest .'
          sh 'docker push tesqos/demojd:latest'
        }
      }

      stage('Deploy locally'){
        steps('Install in pip repository') {
          sh 'echo y | pip uninstall demojd'
          sh 'rm -r -f dist'
          sh 'python setup.py sdist'
//        sh 'pip install dist/*'
          sh 'python3 -m twine upload dist/* -u vipervit'
          sh 'pip install --upgrade demojd'
        }
      }

    }
}
