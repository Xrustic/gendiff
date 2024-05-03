#!/usr/bin/env python3
import os


def get_extension(file_path):
    extension = os.path.splitext(file_path)[1]
    return extension[1:]
