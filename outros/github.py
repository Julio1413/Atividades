import git
import os

TOKEN = ""
REPO_URL = "https://github.com/Julio1413/6X2_App"
PASTA_LOCAL = "./repo_sync"

# URL com autenticação
url = REPO_URL.replace(
    "https://",
    f"https://x-access-token:{TOKEN}@"
)

# Clonar ou abrir o repositório
if not os.path.exists(PASTA_LOCAL):
    repo = git.Repo.clone_from(url, PASTA_LOCAL)
else:
    repo = git.Repo(PASTA_LOCAL)

# Pull
repo.git.pull(url, "main")

# Modificar arquivo
with open(os.path.join(PASTA_LOCAL, "dados.txt"), "a") as f:
    f.write("Linha nova...\n")

# Commit
repo.git.add(all=True)
repo.index.commit("Atualização automática")

# Push
repo.git.push(url, "main")