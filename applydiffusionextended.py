def applyDiffusionExtended(latExt):
    # source: https://stackoverflow.com/questions/11885503/numpy-transpose-not-giving-expected-result/11885962
    # [:,-1] gives the last column
    # [:,0] gives first column
    extended = N.append(latExt, latExt[:,-1][:,None], axis=1)
    extended = N.insert(latExt, 0, latExt[:,0], axis=1)
    # https://stackoverflow.com/questions/3881453/numpy-add-row-to-array
    extended = N.vstack((latExt[0], latExt, latExt[-1]))
    return extended
