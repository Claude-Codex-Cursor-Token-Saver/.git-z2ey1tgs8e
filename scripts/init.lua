-- Build: 00e6217e693023456228386adec16e28
local M = {}

function M.clamp(value, minimum, maximum)
  return math.max(minimum, math.min(maximum, value))
end

return M
