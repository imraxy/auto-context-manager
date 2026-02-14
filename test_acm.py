#!/usr/bin/env python3
"""Test suite for Auto Context Manager"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from auto_context_manager import AutoContextManager
import json

def test_init():
    """Test initialization"""
    acm = AutoContextManager()
    assert acm.data_dir.exists(), "Data directory should exist"
    assert acm.projects_file.exists(), "Projects file should exist"
    print("[PASS] test_init")

def test_load_projects():
    """Test loading projects"""
    acm = AutoContextManager()
    projects = acm.load_projects()
    assert "projects" in projects, "Should have projects key"
    assert "current_project" in projects, "Should have current_project key"
    assert "default" in projects["projects"], "Should have default project"
    print("[PASS] test_load_projects")

def test_detect_project():
    """Test project detection"""
    acm = AutoContextManager()

    # Test trading keywords
    proj, conf = acm.detect_project("show me my binance positions")
    assert proj == "trading", f"Expected 'trading', got '{proj}'"

    # Test clawdbot keywords
    proj, conf = acm.detect_project("check gateway status")
    assert proj == "clawdbot", f"Expected 'clawdbot', got '{proj}'"

    # Test network keywords
    proj, conf = acm.detect_project("connect to pi server")
    assert proj == "network", f"Expected 'network', got '{proj}'"

    # Test default fallback
    proj, conf = acm.detect_project("hello there")
    assert proj == "default", f"Expected 'default', got '{proj}'"

    print("[PASS] test_detect_project")

def test_switch_project():
    """Test project switching"""
    acm = AutoContextManager()

    result = acm.switch_project("trading")
    assert "trading" in result, f"Switch message should mention 'trading'"

    current = acm.get_current_project()
    assert current == "trading", f"Current should be 'trading', got '{current}'"

    # Switch back to default
    acm.switch_project("default")
    print("[PASS] test_switch_project")

def test_list_projects():
    """Test listing projects"""
    acm = AutoContextManager()
    output = acm.list_projects()

    assert "Available Projects" in output, "Should have header"
    assert "trading" in output, "Should list trading project"
    assert "clawdbot" in output, "Should list clawdbot project"
    print("[PASS] test_list_projects")

def test_cli():
    """Test CLI wrapper"""
    import subprocess
    os.chdir(os.path.dirname(__file__))

    # Test detect
    result = subprocess.run(
        [sys.executable, "acm.py", "detect", "binance positions"],
        capture_output=True, text=True, encoding='utf-8'
    )
    assert result.returncode == 0, f"CLI detect failed: {result.stderr}"
    assert "trading" in result.stdout, f"Expected 'trading' in output: {result.stdout}"

    # Test list
    result = subprocess.run(
        [sys.executable, "acm.py", "list"],
        capture_output=True, text=True, encoding='utf-8'
    )
    assert result.returncode == 0, f"CLI list failed: {result.stderr}"

    # Test current
    result = subprocess.run(
        [sys.executable, "acm.py", "current"],
        capture_output=True, text=True, encoding='utf-8'
    )
    assert result.returncode == 0, f"CLI current failed: {result.stderr}"

    print("[PASS] test_cli")

def run_all_tests():
    """Run all tests"""
    print("=" * 50)
    print("Auto Context Manager - Test Suite")
    print("=" * 50)
    print()

    tests = [
        test_init,
        test_load_projects,
        test_detect_project,
        test_switch_project,
        test_list_projects,
        test_cli,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"[FAIL] {test.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"[ERROR] {test.__name__}: {e}")
            failed += 1

    print()
    print("=" * 50)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 50)

    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)