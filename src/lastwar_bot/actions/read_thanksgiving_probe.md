
# Read active activity metadata for research.

READ_LUA (function() local m=DataCenter.ActivityListDataManager if not m then return "manager unavailable" end local rows=m.nowActivityList or m.activityList or {} local out={} for _,v in pairs(rows) do if type(v)=="table" then out[#out+1]="id="..tostring(v.id or "?")..",type="..tostring(v.type or "?")..",desc="..tostring(v.desc_info or "?") end end table.sort(out) return table.concat(out," | ") end)() INTO activities

LOG "Active activities: {activities}"
