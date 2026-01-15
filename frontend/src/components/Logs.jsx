import React from 'react';
import { Terminal } from 'lucide-react';

const Logs = ({ logs }) => {
  return (
    <div className="card bg-base-100 shadow-xl border border-base-200 h-full animate-fade-in">
      <div className="card-body flex flex-col h-full">
         <h3 className="card-title text-base font-black uppercase tracking-tight mb-4 flex items-center gap-2">
            <Terminal className="h-5 w-5 text-info" /> Full System Logs
         </h3>
         <div className="bg-base-200/50 rounded-xl p-4 flex-1 overflow-auto border border-base-200 font-mono text-sm space-y-2">
            {logs.map(log => (
              <div key={log.id} className="flex gap-4 border-b border-base-300 pb-2 last:border-0">
                 <span className="text-xs opacity-50 shrink-0 w-20">{log.timestamp}</span>
                 <span className={`font-bold shrink-0 w-20 ${log.type === 'ERROR' ? 'text-error' : 'text-success'}`}>{log.type}</span>
                 <span className="break-all">{log.message}</span>
              </div>
            ))}
            {logs.length === 0 && <span className="opacity-50 italic">No logs available.</span>}
         </div>
      </div>
    </div>
  );
};

export default Logs;