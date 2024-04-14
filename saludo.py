import os

# escribimos la variable de entorno en GITHUB_OUTPUT
def set_github_action_output(output_name, output_value):
    with open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a") as output:
        print(f'{output_name}={output_value}', file=output)

def run():
    nombre = os.getenv('INPUT_NOMBRE', default="John Doe")
    set_github_action_output('saludo', f'Hola, {nombre}!')

if __name__ == '__main__':
    run()