#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 16:20:28 2020

@author: minhuyen
"""

def diffusion(diffusionRate, site, N, NE, E, SE, S, SW, W, NW):
    return (1 - 8*diffusionRate)*site + ((diffusionRate*N) + (diffusionRate*NE) + (diffusionRate*E) + (diffusionRate*SE) + (diffusionRate*S) + (diffusionRate*SW) + (diffusionRate*W) + (diffusionRate*NW)

def reflectingLat(lat):
    latNS = 