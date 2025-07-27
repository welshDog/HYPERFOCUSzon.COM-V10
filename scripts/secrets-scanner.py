#!/usr/bin/env python3
"""
🛡️💎⚡ BROSKI♾️ GIT SECRETS SCANNER ⚡💎🛡️
Pre-commit security scanner to prevent secret leaks
MAX SECURITY, ZERO SECRETS LEAKED!
"""

import os
import re
import sys
import json
from pathlib import Path
from typing import List, Dict, Tuple

class BroskiSecretsScanner:
    def __init__(self):
        self.secrets_patterns = [
            # API Keys and Tokens
            (r'[Aa]pi[_-]?[Kk]ey["\s]*[:=]["\s]*([A-Za-z0-9_\-]{20,})', 'API Key'),
            (r'[Aa]ccess[_-]?[Tt]oken["\s]*[:=]["\s]*([A-Za-z0-9_\-]{20,})', 'Access Token'),
            (r'[Ss]ecret[_-]?[Kk]ey["\s]*[:=]["\s]*([A-Za-z0-9_\-]{20,})', 'Secret Key'),
            (r'[Pp]assword["\s]*[:=]["\s]*([^\s"\']{8,})', 'Password'),
            
            # Database URLs
            (r'postgres://[^\s"\']+', 'Database URL'),
            (r'mysql://[^\s"\']+', 'Database URL'),
            (r'mongodb://[^\s"\']+', 'Database URL'),
            
            # JWT Secrets
            (r'jwt[_-]?secret["\s]*[:=]["\s]*([A-Za-z0-9_\-]{20,})', 'JWT Secret'),
            
            # Discord/Webhook URLs
            (r'https://discord.com/api/webhooks/[^\s"\']+', 'Discord Webhook'),
            (r'https://hooks.slack.com/[^\s"\']+', 'Slack Webhook'),
            
            # GitHub Tokens
            (r'gh[ps]_[A-Za-z0-9_]{36,}', 'GitHub Token'),
            
            # OpenAI Keys
            (r'sk-[A-Za-z0-9]{48}', 'OpenAI API Key'),
            
            # Generic high-entropy strings
            (r'["\']([A-Za-z0-9+/]{40,}={0,2})["\']', 'High Entropy String'),
        ]
        
        self.file_extensions = ['.py', '.js', '.ts', '.json', '.yaml', '.yml', '.env', '.md', '.txt']
        self.ignore_patterns = [
            'node_modules/',
            '.git/',
            'dist/',
            'build/',
            '__pycache__/',
            '.vscode/',
            'showcase/',  # Our demo directory is safe
        ]

    def scan_file(self, file_path: Path) -> List[Dict]:
        """Scan a single file for potential secrets"""
        findings = []
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            for line_num, line in enumerate(content.split('\n'), 1):
                for pattern, secret_type in self.secrets_patterns:
                    matches = re.finditer(pattern, line, re.IGNORECASE)
                    for match in matches:
                        # Skip obvious templates, examples, or regex patterns
                        if any(skip in line.lower() for skip in ['example', 'template', 'demo', 'your_', 'placeholder', 'regex', 'pattern', r'\s', r'\d', '(r\'', 'secrets_patterns']):
                            continue
                            
                        findings.append({
                            'file': str(file_path),
                            'line': line_num,
                            'type': secret_type,
                            'match': match.group(0)[:50] + '...' if len(match.group(0)) > 50 else match.group(0),
                            'context': line.strip()[:100] + '...' if len(line.strip()) > 100 else line.strip()
                        })
                        
        except Exception as e:
            print(f"⚠️  Error scanning {file_path}: {e}")
            
        return findings

    def should_ignore_file(self, file_path: Path) -> bool:
        """Check if file should be ignored"""
        file_str = str(file_path)
        
        # Check ignore patterns
        for pattern in self.ignore_patterns:
            if pattern in file_str:
                return True
                
        # Check file extension
        if file_path.suffix not in self.file_extensions:
            return True
            
        return False

    def scan_directory(self, directory: Path) -> List[Dict]:
        """Scan all files in directory"""
        all_findings = []
        
        for file_path in directory.rglob('*'):
            if file_path.is_file() and not self.should_ignore_file(file_path):
                findings = self.scan_file(file_path)
                all_findings.extend(findings)
                
        return all_findings

    def display_findings(self, findings: List[Dict]) -> None:
        """Display scan results"""
        if not findings:
            print("🎉 SUCCESS: No secrets detected! Safe to commit! 🛡️")
            return
            
        print(f"🚨 DANGER: {len(findings)} potential secrets detected!")
        print("=" * 60)
        
        for finding in findings:
            print(f"📁 File: {finding['file']}")
            print(f"📍 Line: {finding['line']}")
            print(f"🔍 Type: {finding['type']}")
            print(f"🎯 Match: {finding['match']}")
            print(f"📝 Context: {finding['context']}")
            print("-" * 40)
            
        print("\n🛡️ RECOMMENDATIONS:")
        print("1. Remove secrets and use environment variables")
        print("2. Add sensitive files to .gitignore")  
        print("3. Use config templates instead of real secrets")
        print("4. Join Discord for security best practices!")
        print("\n👉 Discord: https://discord.com/invite/ME2qkNy79k 👈")

def main():
    """Main scanner entry point"""
    print("🛡️💎 BROski♾️ Git Secrets Scanner - LEGENDARY SECURITY MODE! 💎🛡️")
    print()
    
    # Get directory to scan
    scan_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    
    if not scan_dir.exists():
        print(f"❌ Directory {scan_dir} does not exist!")
        sys.exit(1)
        
    print(f"🔍 Scanning directory: {scan_dir.absolute()}")
    print()
    
    # Initialize scanner and run
    scanner = BroskiSecretsScanner()
    findings = scanner.scan_directory(scan_dir)
    
    # Display results
    scanner.display_findings(findings)
    
    # Exit with error code if secrets found
    if findings:
        print(f"\n🚫 COMMIT BLOCKED: Fix {len(findings)} security issues first!")
        sys.exit(1)
    else:
        print("\n✅ COMMIT APPROVED: All security checks passed!")
        sys.exit(0)

if __name__ == "__main__":
    main()
