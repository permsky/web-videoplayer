from livereload import Server


server = Server()
server.watch('index.html')
server.serve(
    root='.',
    port=8080,
    host='localhost',
    default_filename='index.html'
)
        