#!/usr/bin/env python
# -*- coding: utf-8 -*-

# GRID-BASED PLUGIN FOR GIMP
# Version: 3.0
# License: GPLv3
# Author: Sergey Grigorev (issetname@gmail.com)
# Link project: https://github.com/gsaone/grid-based-plugin-for-gimp

from gimpfu import *

def add_border(image):
    non_empty, x1, y1, x2, y2 = pdb.gimp_selection_bounds(image)
    if non_empty: # for selection
        guide = pdb.gimp_image_add_vguide(image, x1)
        guide = pdb.gimp_image_add_hguide(image, y1)
        guide = pdb.gimp_image_add_vguide(image, x2)
        guide = pdb.gimp_image_add_hguide(image, y2)        
    else: # for full image
        guide = pdb.gimp_image_add_vguide(image, 0)
        guide = pdb.gimp_image_add_vguide(image, pdb.gimp_image_width(image))
        guide = pdb.gimp_image_add_hguide(image, 0)
        guide = pdb.gimp_image_add_hguide(image, pdb.gimp_image_height(image))
    
def add_center(image):
    non_empty, x1, y1, x2, y2 = pdb.gimp_selection_bounds(image)
    if non_empty: # for selection
        guide = pdb.gimp_image_add_vguide(image, (x2 - x1) / 2 + x1)
        guide = pdb.gimp_image_add_hguide(image, (y2 - y1) / 2 + y1)
    else: # for full image
        guide = pdb.gimp_image_add_vguide(image, pdb.gimp_image_width(image)/2)
        guide = pdb.gimp_image_add_hguide(image, pdb.gimp_image_height(image)/2)
    
def add_table(image, column, row, gutter):
    non_empty, x1, y1, x2, y2 = pdb.gimp_selection_bounds(image)
    if non_empty: # for selection
        if column > 0:
            size = ((x2 - x1) - (gutter * (column + 1))) / column
            for count in range(column + 1):
                if count == 0:
                    guide = pdb.gimp_image_add_vguide(image, gutter + x1)
                elif count > 0 and count < column:
                    guide = pdb.gimp_image_add_vguide(image, ((size + gutter) * count + gutter) + x1)
                    guide = pdb.gimp_image_add_vguide(image, ((size + gutter) * count) + x1)
                else:
                    guide = pdb.gimp_image_add_vguide(image, ((size + gutter) * count) + x1)
        if row > 0:
            size = ((y2 - y1) - (gutter * (row + 1))) / row
            for count in range(row + 1):
                if count == 0:
                    guide = pdb.gimp_image_add_hguide(image, gutter + y1)
                elif count > 0 and count < row:
                    guide = pdb.gimp_image_add_hguide(image, ((size + gutter) * count + gutter) + y1)
                    guide = pdb.gimp_image_add_hguide(image, ((size + gutter) * count) + y1)
                else:
                    guide = pdb.gimp_image_add_hguide(image, ((size + gutter) * count) + y1)
    else: # for full image
        if column > 0:
            size = (pdb.gimp_image_width(image) - (gutter * (column + 1))) / column
            for count in range(column + 1):
                if count == 0:
                    guide = pdb.gimp_image_add_vguide(image, gutter)
                elif count > 0 and count < column:
                    guide = pdb.gimp_image_add_vguide(image, (size + gutter) * count + gutter)
                    guide = pdb.gimp_image_add_vguide(image, (size + gutter) * count)
                else:
                    guide = pdb.gimp_image_add_vguide(image, (size + gutter) * count)
        if row > 0:
            size = (pdb.gimp_image_height(image) - (gutter * (row + 1))) / row
            for count in range(row + 1):
                if count == 0:
                    guide = pdb.gimp_image_add_hguide(image, gutter)
                elif count > 0 and count < row:
                    guide = pdb.gimp_image_add_hguide(image, (size + gutter) * count + gutter)
                    guide = pdb.gimp_image_add_hguide(image, (size + gutter) * count)
                else:
                    guide = pdb.gimp_image_add_hguide(image, (size + gutter) * count)

def add_grid_based(image, drawable, borders, center, column, row, gutter):
    pdb.gimp_context_push()
    pdb.gimp_image_undo_group_start(image)
    
    if borders:
        add_border(image)
    if center:
        add_center(image)    
    add_table(image, column, row, gutter)
    
    pdb.gimp_image_undo_group_end(image)
    pdb.gimp_context_pop()
    
register("python-fu-add-grid-based","Grid-based plugin for gimp","Add grid-based layout",
         "","","","Add grid-based","*",
         [
          (PF_IMAGE, "image", "Source image", None),
          (PF_DRAWABLE, "drawable", "Source layer", None),
          (PF_BOOL,   "borders", "Borders", False),
          (PF_BOOL,   "center", "Center", False),
          (PF_INT, "column", "Column", "0"),
          (PF_INT, "row", "Row", "0"),
          (PF_FLOAT, "gutter", "Gutter", "0.0")
          ],[],
         add_grid_based, menu="<Image>/Tools/Grid-based/")
main()
