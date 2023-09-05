# %%
import subprocess
import sys
import msvcrt

def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except Exception as e:
        print(f"An error occurred while installing the package: {e}")
        return

# Path to your module directory
package_path = '.'

install_package(package_path)

# Check if script is running in IPython kernel (like Jupyter)
if not 'get_ipython' in globals():
    # Not running in IPython, so prompt for key press
    print("Press any key to continue...")
    msvcrt.getch()

# %%
