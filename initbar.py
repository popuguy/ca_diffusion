def initBar(m, n, hotSites, coldSites):
    """initBar(m, n, hotSites, coldSites)Function to return an m×n grid of
     temperatures: Cells with coordinates in hotSites have the value HOT;
      cells with coordinates in coldSites have the value COLD; and all other
      cells have the value AMBIENT
      Pre:m and n are positive integers.hotSites
       and coldSites are lists of coordinates for hot and cold sites,
       respectively.AMBIENT, HOT, and COLD are global constants, and
       COLD≤AM-BIENT≤HOT.
       Post:An m×n grid of values as described before has
       been returned.
       Algorithm:
       ambientBar←m by n matrix of AMBIENT values
       return          applyHotCold(ambientBar, hotSites, coldSites)"""
       ambientBar = N.ones((m, n)) * AMBIENT
       # for i in range(m):
       #     for j in range(n):
       #
       return applyHotCold(ambintBar, hotSites, coldSites)
