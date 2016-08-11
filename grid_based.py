#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import *


def add_grid_guides(image, drawable, gborders, gcenter, column, row, spacing):
  
  pdb.gimp_context_push()
  pdb.gimp_image_undo_group_start(image)

  # add guide borders
  if gborders:
    guide = pdb.gimp_image_add_vguide(image, 0)
    guide = pdb.gimp_image_add_vguide(image, pdb.gimp_image_width(image))
    guide = pdb.gimp_image_add_hguide(image, 0)
    guide = pdb.gimp_image_add_hguide(image, pdb.gimp_image_height(image))

  # add guide center
  if gcenter:
    guide = pdb.gimp_image_add_vguide(image, pdb.gimp_image_width(image)/2)
    guide = pdb.gimp_image_add_hguide(image, pdb.gimp_image_height(image)/2)

  # add guide columns
  if column > 0:
    column_size = (pdb.gimp_image_width(image) - (spacing * (column + 1))) / column
    i = 0
    while i <= column:
      if i == 0:
        guide = pdb.gimp_image_add_vguide(image, spacing)
      elif i > 0 and i < column:
        guide = pdb.gimp_image_add_vguide(image, (column_size+spacing)*i+spacing)
        guide = pdb.gimp_image_add_vguide(image, (column_size+spacing)*i)
      else:
        guide = pdb.gimp_image_add_vguide(image, (column_size+spacing)*i)
      i = i+1

  # add guide rows
  if row > 0:
    row_size = (pdb.gimp_image_height(image) - (spacing * (row + 1))) / row
    i = 0
    while i <= row:
      if i == 0:
        guide = pdb.gimp_image_add_hguide(image, spacing)
      elif i > 0 and i < row:
        guide = pdb.gimp_image_add_hguide(image, (row_size+spacing)*i+spacing)
        guide = pdb.gimp_image_add_hguide(image, (row_size+spacing)*i)
      else:
        guide = pdb.gimp_image_add_hguide(image, (row_size+spacing)*i)
      i = i+1  

  pdb.gimp_image_undo_group_end(image)
  pdb.gimp_context_pop()


register(
          "python-fu-add-grid-guides",
          "Add grid guides",
          "Add grid guides",
          "Sergey Grigorev",
          "Sergey Grigorev (issetname@gmail.com)",
          "11-08-2016",
          "Add grid guides",
          "*",
          [
              (PF_IMAGE, "image", "Source image", None),
              (PF_DRAWABLE, "drawable", "Source layer", None),
              (PF_BOOL,   "gborders", "Borders", False),
              (PF_BOOL,   "gcenter", "Center", False),
              (PF_INT, "column", "Column", "0"),
              (PF_INT, "row", "Row", "0"),
              (PF_FLOAT, "spacing", "Spacing", "0.0")
              
          ],
          [],
          add_grid_guides, menu="<Image>/Grid-based/")

main()
