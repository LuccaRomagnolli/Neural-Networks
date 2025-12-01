#!/usr/bin/env python3
"""
Script para verificar se o ambiente está configurado corretamente
Snake AI - PyTorch
"""

import sys
import os

def check_dependencies():
    """Verifica se todas as dependências estão instaladas"""
    print("🔍 Verificando dependências...\n")
    
    dependencies = {
        'torch': 'PyTorch',
        'pygame': 'Pygame',
        'numpy': 'NumPy',
        'matplotlib': 'Matplotlib',
        'IPython': 'IPython'
    }
    
    all_ok = True
    for module, name in dependencies.items():
        try:
            mod = __import__(module)
            version = getattr(mod, '__version__', 'desconhecida')
            print(f"✅ {name} {version} - OK")
        except ImportError as e:
            print(f"❌ {name} - ERRO: {e}")
            all_ok = False
    
    return all_ok

def check_project_files():
    """Verifica se os arquivos do projeto existem"""
    print("\n📁 Verificando arquivos do projeto...\n")
    
    required_files = [
        'agent.py',
        'game.py',
        'model.py',
        'helper.py',
        'snake_game_human.py',
        'arial.ttf',
        'pyproject.toml'
    ]
    
    all_ok = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} - OK")
        else:
            print(f"❌ {file} - NÃO ENCONTRADO")
            all_ok = False
    
    return all_ok

def check_project_modules():
    """Verifica se os módulos do projeto podem ser importados"""
    print("\n📦 Verificando módulos do projeto...\n")
    
    modules = [
        ('game', 'SnakeGameAI, Direction, Point'),
        ('model', 'Linear_QNet, QTrainer'),
        ('helper', 'plot'),
        ('agent', 'Agent')
    ]
    
    all_ok = True
    for module_name, exports in modules:
        try:
            mod = __import__(module_name)
            print(f"✅ {module_name}.py - Importação OK")
        except Exception as e:
            print(f"❌ {module_name}.py - ERRO: {e}")
            all_ok = False
    
    return all_ok

def main():
    """Função principal"""
    print("=" * 50)
    print("🐍 Snake AI - Verificação de Configuração")
    print("=" * 50)
    print()
    
    deps_ok = check_dependencies()
    files_ok = check_project_files()
    modules_ok = check_project_modules()
    
    print("\n" + "=" * 50)
    if deps_ok and files_ok and modules_ok:
        print("✅ TUDO CONFIGURADO CORRETAMENTE!")
        print("\n🚀 Você pode executar:")
        print("   - python3 agent.py          (Treinar a IA)")
        print("   - python3 snake_game_human.py  (Jogar manualmente)")
        print("   - ./run_training.sh        (Script de treinamento)")
        print("   - ./run_human.sh           (Script modo humano)")
        return 0
    else:
        print("❌ ALGUNS PROBLEMAS FORAM ENCONTRADOS")
        print("\n💡 Soluções:")
        if not deps_ok:
            print("   - Execute: pip3 install -e .")
        if not files_ok:
            print("   - Verifique se está no diretório correto")
        if not modules_ok:
            print("   - Verifique os erros acima e corrija os problemas")
        return 1

if __name__ == '__main__':
    sys.exit(main())

