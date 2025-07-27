#!/usr/bin/env python3
"""
🚀💎⚡ BROSKI♾️ REPOSITORY SETUP AUTOMATION ⚡💎🚀
One-click setup for the LEGENDARY EMPIRE showcase repository
"""

import os
import stat
import subprocess
from pathlib import Path

def setup_git_hooks():
    """Make pre-commit hook executable"""
    hook_path = Path('.git/hooks/pre-commit')
    if hook_path.exists():
        # Make executable on Unix systems
        try:
            current_permissions = hook_path.stat().st_mode
            hook_path.chmod(current_permissions | stat.S_IEXEC)
            print("✅ Pre-commit hook made executable")
        except:
            print("ℹ️  Pre-commit hook permissions set (Windows)")
    else:
        print("⚠️  Pre-commit hook not found")

def check_python():
    """Verify Python is available"""
    try:
        result = subprocess.run(['python', '--version'], capture_output=True, text=True)
        print(f"✅ Python available: {result.stdout.strip()}")
        return True
    except:
        try:
            result = subprocess.run(['python3', '--version'], capture_output=True, text=True)
            print(f"✅ Python3 available: {result.stdout.strip()}")
            return True
        except:
            print("❌ Python not found! Install Python to use security scanner.")
            return False

def run_initial_scan():
    """Run the secrets scanner"""
    print("\n🛡️ Running initial security scan...")
    try:
        result = subprocess.run(['python', 'scripts/secrets-scanner.py', '.'], 
                              capture_output=True, text=True)
        print(result.stdout)
        if result.returncode == 0:
            print("🎉 Repository is secure and ready for deployment!")
            return True
        else:
            print("🚨 Security issues detected. Fix them before deploying!")
            return False
    except Exception as e:
        print(f"⚠️  Could not run security scan: {e}")
        return False

def main():
    print("🚀💎 BROski♾️ Repository Setup - LEGENDARY EMPIRE MODE! 💎🚀")
    print()
    
    # Check Python
    if not check_python():
        return
    
    # Setup Git hooks
    setup_git_hooks()
    
    # Run initial scan
    secure = run_initial_scan()
    
    print("\n" + "="*60)
    print("🎯 SETUP COMPLETE!")
    print()
    print("📝 Next Steps:")
    print("1. Review the DEPLOYMENT_CHECKLIST.md")
    print("2. Test the pre-commit hook: git commit -m 'test'")
    print("3. Join the Discord community for empire access!")
    print("4. Push to showcase the LEGENDARY EMPIRE!")
    print()
    print("👉 Discord: https://discord.com/invite/ME2qkNy79k 👈")
    print("💎 Ready to conquer the coding world! 💎")

if __name__ == "__main__":
    main()
