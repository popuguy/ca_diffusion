def applyDiffusionExtended(latExt):
    # source: https://stackoverflow.com/questions/11885503/numpy-transpose-not-giving-expected-result/11885962
    # [:,-1] gives the last column
    # [:,0] gives first column
    # extended = N.append(latExt, latExt[:,-1][:,None], axis=1)
    # extended = N.insert(latExt, 0, latExt[:,0], axis=1)
    # # https://stackoverflow.com/questions/3881453/numpy-add-row-to-array
    # extended = N.vstack((latExt[0], latExt, latExt[-1]))
    # # return extended
    #
    result = N.copy(latExt)
    for row in range(1, latExt.shape[0] - 1):
        for col in range(1, latExt.shape[1] - 1):
            N = latExt[row - 1][col]
            NE = latExt[row - 1][col + 1]
            E = latExt[row][col + 1]
            SE = latExt[row - 1][col + 1]
            S = latExt[row - 1][col]
            SW = latExt[row - 1][col - 1]
            W = latExt[row][col - 1]
            NW = latExt[row - 1][col - 1]
            result[row][col] = diffusion(diffusionRate, \
                                latExt[row][col], N, NE, E, SE, S, SW, W, NW)
    return result[1:-1,1:-1]
