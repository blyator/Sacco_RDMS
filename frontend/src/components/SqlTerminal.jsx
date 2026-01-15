import React from 'react';

const SqlTerminal = ({ sqlQuery, setSqlQuery, sqlResult, handleExecuteSQL }) => {
  return (
    <div className="grid grid-cols-1 lg:grid-cols-4 gap-8 animate-fade-in h-full pb-10">
       <div className="lg:col-span-3 space-y-6">
          <div className="card bg-base-100 shadow-xl border border-base-200">
             <div className="card-body">
                <h3 className="text-xs font-black opacity-40 uppercase tracking-widest mb-2">Execute Command</h3>
                <textarea 
                  className="textarea textarea-bordered font-mono w-full h-32 text-lg bg-base-200 text-base-content focus:outline-primary"
                  placeholder="SELECT * FROM members WHERE member_id = 101"
                  value={sqlQuery}
                  onChange={e => setSqlQuery(e.target.value)}
                />
                <div className="card-actions justify-end mt-2">
                   <button className="btn btn-primary px-8 font-black uppercase tracking-wider" onClick={handleExecuteSQL}>Execute</button>
                </div>
             </div>
          </div>

          <div className="card bg-base-300 shadow-inner border border-base-content/10">
             <div className="card-body p-0">
                <div className="px-6 py-3 border-b border-base-content/10 flex items-center justify-between bg-base-content/5">
                   <span className="text-xs font-black opacity-50 uppercase tracking-widest">Query Result</span>
                   <div className="flex gap-1.5">
                      <div className="w-2.5 h-2.5 rounded-full bg-error"></div>
                      <div className="w-2.5 h-2.5 rounded-full bg-warning"></div>
                      <div className="w-2.5 h-2.5 rounded-full bg-success"></div>
                   </div>
                </div>
                <div className="p-6 overflow-auto font-mono text-sm min-h-[300px] bg-base-100">
                   {!sqlResult && <span className="opacity-50 italic">// Ready for command...</span>}
                   {sqlResult && sqlResult.status === 'error' && <div className="text-error font-bold">ERROR: {sqlResult.data}</div>}
                   {sqlResult && sqlResult.status === 'success' && (
                      Array.isArray(sqlResult.data) ? (
                         <table className="table table-xs w-full">
                            <thead className="text-primary border-b border-base-200">
                               <tr>{sqlResult.data.length > 0 && Object.keys(sqlResult.data[0]).map(k => <th key={k}>{k}</th>)}</tr>
                            </thead>
                            <tbody>
                               {sqlResult.data.map((row, i) => (
                                  <tr key={i} className="hover">
                                     {Object.values(row).map((val, j) => <td key={j}>{val}</td>)}
                                  </tr>
                               ))}
                            </tbody>
                         </table>
                      ) : (
                         <div className="text-success">{JSON.stringify(sqlResult.data, null, 2)}</div>
                      )
                   )}
                </div>
             </div>
          </div>
       </div>

       <div className="lg:col-span-1">
          <div className="card bg-base-100 shadow-xl border border-base-200 h-full">
             <div className="card-body">
                <h3 className="card-title text-sm font-black opacity-40 uppercase tracking-widest mb-4 border-b border-base-200 pb-2">Templates</h3>
                <ul className="menu bg-base-200 w-full rounded-box">
                   <li><a onClick={() => setSqlQuery('SELECT * FROM members')} className="text-xs font-bold">Get All Members</a></li>
                   <li><a onClick={() => setSqlQuery('SELECT * FROM accounts')} className="text-xs font-bold">Get All Accounts</a></li>
                   <li><a onClick={() => setSqlQuery("INSERT INTO members VALUES (99, 'NEW USER', 'ID001')")} className="text-xs font-bold">Add Member SQL</a></li>
                </ul>
                <div className="mt-auto pt-4 border-t border-base-200">
                   <p className="text-[10px] opacity-50 font-medium leading-relaxed">Type direct SQL commands to interact with the custom RDMS engine.</p>
                </div>
             </div>
          </div>
       </div>
    </div>
  );
};

export default SqlTerminal;