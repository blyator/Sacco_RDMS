import React from 'react';
import { TrendingUp, Terminal } from 'lucide-react';

const Dashboard = ({ statCards, members, logs, fetchData }) => {
  return (
    <div className="space-y-8 animate-fade-in pb-10">
      {/* Stats Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {statCards.map((stat, index) => {
          const Icon = stat.icon;
          return (
            <div key={index} className="card bg-base-100 shadow-xl border border-base-200">
              <div className="card-body p-6">
                <div className="flex items-center justify-between mb-2">
                   <h3 className="text-xs font-black opacity-50 uppercase tracking-widest">{stat.title}</h3>
                   <Icon className={`h-6 w-6 ${stat.color}`} />
                </div>
                <div className="text-3xl font-black">{stat.value}</div>
                <p className="text-xs opacity-60 font-medium">{stat.description}</p>
              </div>
            </div>
          );
        })}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Top Members */}
        <div className="card bg-base-100 shadow-xl border border-base-200 h-fit">
          <div className="card-body p-0">
             <div className="p-4 border-b border-base-200 flex items-center justify-between bg-base-200/30">
                <h2 className="card-title text-base font-black uppercase tracking-tight flex items-center gap-2">
                   <TrendingUp className="h-5 w-5 text-primary" /> Recent Members
                </h2>
                <button onClick={fetchData} className="btn btn-ghost btn-xs">Refresh</button>
             </div>
             <div className="overflow-x-auto">
               <table className="table table-zebra w-full">
                  <thead className="bg-base-200/50 text-xs font-black uppercase opacity-60">
                     <tr>
                        <th>ID</th>
                        <th>Full Name</th>
                        <th>National ID</th>
                     </tr>
                  </thead>
                  <tbody>
                     {members.slice(0, 5).map(m => (
                       <tr key={m.member_id}>
                          <th className="font-mono text-primary">#{m.member_id}</th>
                          <td className="font-bold uppercase">{m.name}</td>
                          <td className="opacity-70">{m.national_id}</td>
                       </tr>
                     ))}
                     {members.length === 0 && <tr><td colSpan="3" className="text-center py-8 opacity-50">No records found</td></tr>}
                  </tbody>
               </table>
             </div>
          </div>
        </div>

        {/* Recent Activity */}
        <div className="card bg-base-100 shadow-xl border border-base-200 h-fit">
           <div className="card-body p-0">
             <div className="p-4 border-b border-base-200 flex items-center gap-2 bg-base-200/30">
                <Terminal className="h-5 w-5 text-secondary" />
                <h2 className="card-title text-base font-black uppercase tracking-tight">System Logs</h2>
             </div>
             <div className="p-4 space-y-4">
              {logs.length > 0 ? (
                logs.slice(0, 6).map((log) => (
                  <div key={log.id} className="flex items-center justify-between group border-b border-base-200 pb-2 last:border-0 last:pb-0">
                    <div className="flex items-center gap-3">
                       <div className={`badge badge-xs ${log.type === 'ERROR' ? 'badge-error' : 'badge-success'}`}></div>
                       <div>
                          <p className="text-sm font-bold">{log.message}</p>
                          <p className="text-[10px] opacity-50 font-black uppercase">{log.type} • {log.timestamp}</p>
                       </div>
                    </div>
                  </div>
                ))
              ) : (
                <p className="text-sm opacity-50 text-center py-8 font-medium italic">No activity recorded yet</p>
              )}
             </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;